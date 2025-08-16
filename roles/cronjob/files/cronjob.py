#! /usr/bin/python3
import shlex
from argparse import ArgumentParser
from re import compile
from subprocess import run
from typing import TypedDict
from unittest import TestCase

from apprise import Apprise


class RunResult(TypedDict):
    success: bool
    out: str


def build_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('--avatar', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--webhook-id', required=True)
    parser.add_argument('--webhook-token', required=True)
    parser.add_argument('--dont-notify-if')
    parser.add_argument('--always-ping', type=bool, default=False)
    parser.add_argument('--command', required=True)
    return parser


def run_command(command: str) -> RunResult:
    process = run(shlex.split(command), capture_output=True, text=True)
    success = process.returncode == 0
    return {
        "success": success,
        "out": process.stdout if success else process.stderr
    }


def build_notification(result: RunResult, always_ping: bool) -> str:
    body = f"```\n{result['out']}\n```"
    if always_ping or not result['success']:
        body = "@here\n" + body
    if not result['success']:
        body = "**Failed**\n" + body
    return body


if __name__ == '__main__':
    args = build_parser().parse_args()
    dont_notify_if = compile(args.dont_notify_if) if args.dont_notify_if else None
    run_result = run_command(args.command)
    if dont_notify_if and dont_notify_if.match(run_result['out']):
        exit(0)
    apprise = Apprise(servers=f"discord://{args.name}@{args.webhook_id}/{args.webhook_token}/?avatar_url={args.avatar}")
    apprise.notify(build_notification(run_result, args.always_ping))


class Tests(TestCase):
    def test_parser(self):
        args = build_parser().parse_args([
            "--avatar", "https://cdn.jsdelivr.net/gh/selfhst/icons/png/docker.png",
            "--name", "Docker Image Prune",
            "--webhook-id", "cool-id-with-dashes",
            "--webhook-token", "Num3ric4lStr1ingW1th-Dashesss",
            "--dont-notify-if", "$\\w*^",
            "--always-ping", "true",
            "--command", "docker image prune"
        ])
        self.assertEqual('https://cdn.jsdelivr.net/gh/selfhst/icons/png/docker.png', args.avatar)
        self.assertEqual('Docker Image Prune', args.name)
        self.assertEqual('cool-id-with-dashes', args.webhook_id)
        self.assertEqual('Num3ric4lStr1ingW1th-Dashesss', args.webhook_token)
        self.assertTrue(args.always_ping)
        self.assertEqual('docker image prune', args.command)

    def test_run_command_success(self):
        result = run_command('echo Command successful!')
        self.assertTrue(result['success'])
        self.assertEqual(result['out'], 'Command successful!\n')

    def test_run_command_failed(self):
        result = run_command('man quatsch\\ with\\ sauce')
        self.assertFalse(result['success'])
        self.assertEqual(result['out'], "No manual entry for quatsch with sauce\n")

    def test_build_notification_success(self):
        self.assertEqual(
            "```\nEverything alright~\n```",
            build_notification({"success": True, "out": "Everything alright~"}, False)
        )

    def test_build_notification_always_ping(self):
        self.assertEqual(
            "@here\n```\nThere are updates!\n```",
            build_notification({"success": True, "out": "There are updates!"}, True)
        )

    def test_build_notification_failed(self):
        self.assertEqual(
            "**Failed**\n@here\n```\nBorked!\n```",
            build_notification({"success": False, "out": "Borked!"}, False)
        )
