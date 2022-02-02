# symmetric-secrete-share

CLI to share secret files via github with symmetric encryption ed25519.

- **IMPORTANT: The secret files at should be git-ignored to avoid oblivious leakage.**
- Temporarily supports only text files (only tested with `.env`).
- Best used to store secrets and configurations.
- Key should be a 32-byte long string.
- (FAQ) If you share with GitHub, please notice that there's a 5 minutes cool-down on refreshing. [Details](https://stackoverflow.com/questions/46551413/github-not-update-raw-after-commit)

## Use

1. Install CLI `pip3 install symmetric-secrete-share`.
2. Check the [Tutorial Chapter](#Tutorial) and `sss --help`.
3. Recommended: set up a global key chain with `sss key`, or you would have to input key every time.
4. Get a config like `$REPO_ROOT/test/injection/sss.json`. The json-schema inside will help you write it.

### inject

1. Get a config file like `$REPO_ROOT/test/injection/sss.json`. The json-schema inside will help you write it.
2. run CLI

   ```bash
   sss inject [-k TEXT] CONFIG_PATH
   ```

### share

1. Run CLI

   ```bash
   sss share [-k TEXT] CONFIG_PATH
   ```

2. Upload the generated file to GitHub (or other platforms).
3. Update the config file if needed.

## Contribute

- Created for [Artcoin-Network](https://github.com/Artcoin-Network/), modifying the private repo [Artcoin-Network/artificial-dev-config](https://github.com/Artcoin-Network/artificial-dev-config).
- To contribute, please fork the repo and run `poetry install`.
- Read more in [dev-docs.md](./docs/dev-docs.md)

## Tutorial

In this tutorial, all commands are assumed to run under the `$REPO_ROOT`. We are going to use these concepts:

- key: `This key contains 32 characters.`.
- URL: `https://raw.githubusercontent.com/PabloLION/symmetric-secrete-share/main/tests/example.encrypted`.
- key chain: A file to share key, initialized with `sss key`.

We are going to play with the folder `test/injection`, with the `sss.json` file inside it. To share your own file, a new config file should be created.

### Setup a local key chain

```bash
sss key # create/edit
sss key -c # clear all keys
```

### load files from URL

These code will generate a `test/injection/target.env` like `test/example.env`

```bash
sss inject ./tests/injection/sss.json # use key from initial key chain
sss inject -k "This key contains 32 characters." ./tests/injection/sss.json
sss inject ./tests/injection/sss.json -k "I'm a string with 32 characters." # fail
```

### share files

Need to upload manually #TODO
These code will generate a `test/injection/target.encrypted`

```bash
sss share ./tests/injection/sss.json # use key from initial key chain
sss share -k "This key contains 32 characters." ./tests/injection/sss.json
```
