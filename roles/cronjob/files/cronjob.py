#! /usr/bin/python3
from typing import Sequence, TypedDict

from apprise import Apprise
from argparse import ArgumentParser
from subprocess import run
from unittest import TestCase

class RunResult(TypedDict):
    success: bool
    out: str

def build_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('--avatar', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--webhook-id', required=True)
    parser.add_argument('--webhook-token', required=True)
    parser.add_argument('--command', required=True)
    return parser

def run_command(command: str) -> RunResult:
    process = run(command.split(' '), capture_output=True, text=True)
    success = process.returncode == 0
    return {
        "success": success,
        "out": process.stdout if success else process.stderr
    }

def build_notification(result: RunResult) -> str:
    body = f"```\n{result['out']}\n```"
    if result['success']:
        return body
    return f"**Failed** @here\n{body}"


if __name__ == '__main__':
    args = build_parser().parse_args()
    run_result = run_command(args.command)
    apprise = Apprise(servers=f"discord://{args.name}@{args.webhook_id}/{args.webhook_token}/?avatar_url={args.avatar}")
    apprise.notify(build_notification(run_result))

class Tests(TestCase):
    def test_parser(self):
        args = build_parser().parse_args([
            "--avatar", "https://cdn.jsdelivr.net/gh/selfhst/icons/png/docker.png",
            "--name", "Docker Image Prune",
            "--webhook-id", "cool-id-with-dashes",
            "--webhook-token", "Num3ric4lStr1ingW1th-Dashesss",
            "docker", "image", "prune"
        ])
        self.assertEqual('https://cdn.jsdelivr.net/gh/selfhst/icons/png/docker.png', args.avatar)
        self.assertEqual('Docker Image Prune', args.name)
        self.assertEqual('cool-id-with-dashes', args.webhook_id)
        self.assertEqual('Num3ric4lStr1ingW1th-Dashesss', args.webhook_token)
        self.assertEqual(['docker', 'image', 'prune'], args.command)

    def test_run_command_success(self):
        result = run_command(["echo", "Command successful!"])
        self.assertTrue(result['success'])
        self.assertEqual(result['out'], "Command successful!\n")

    def test_run_command_failed(self):
        result = run_command(["man", "quatsch with sauce"])
        self.assertFalse(result['success'])
        self.assertEqual(result['out'], "No manual entry for quatsch with sauce\n")

    def test_build_notification_success(self):
        self.assertEqual(
            "```\nEverything alright~\n```",
            build_notification({"success": True, "out": "Everything alright~"})
        )
    def test_build_notification_failed(self):
        self.assertEqual(
            "**Failed** @here\n```\nBorked!\n```",
            build_notification({"success": False, "out": "Borked!"})
        )
