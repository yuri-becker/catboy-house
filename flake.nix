{
  description = "Shell for catboy.house project.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "aarch64-darwin" "x86_64-linux" ];
      perSystem = { pkgs, ... }: {
        devShells.default = with pkgs; mkShell {
          packages = [ ansible fish just ];
          shellHook = ''
            exec fish
          '';
        };
      };
    };
}
