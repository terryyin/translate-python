{
  description = "Python translate CLI development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        python = pkgs.python3;
        pythonPackages = pkgs.python3Packages;
      in
      {
        devShells.default = pkgs.mkShell {
          name = "translate-python";
          
          MYSQL_HOME = builtins.getEnv "MYSQL_HOME";
          MYSQL_DATADIR = builtins.getEnv "MYSQL_DATADIR";
          
          buildInputs = with pkgs; [
            python
            pythonPackages.pip
            pythonPackages.setuptools
            pythonPackages.wheel
            vim
            git
          ];
          
          shellHook = ''
            export PYTHONUSERBASE=$PWD/.local
            export USER_SITE=$(python -c "import site; print(site.USER_SITE)")
            
            # Fix Python version in USER_SITE path if needed
            export USER_SITE=${"\$\{USER_SITE//3.8/3.9}"}
            
            export PYTHONPATH=$PYTHONPATH:$USER_SITE
            export PATH=$PATH:$PYTHONUSERBASE/bin
            
            echo "Development environment ready!"
            echo "Install dependencies with: pip install --user -r requirements-dev.txt"
            echo "Run tests with: pytest"
          '';
        };
      }
    );
}

