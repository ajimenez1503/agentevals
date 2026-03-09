# Development Guide

## Distribution tiers

agentevals ships as three distinct configurations from a single codebase:

| Tier | Install | Serve behavior |
|------|---------|----------------|
| **Core** | `pip install agentevals` | REST API only — stateless batch evaluation endpoints |
| **Live** | `pip install "agentevals[live]"` | REST API + WebSocket streaming + session management + MCP |
| **Bundle** | `pip install "agentevals[live]"` (bundled wheel) | Live + embedded React UI served at root |

The `[live]` extra adds `mcp` and `httpx`. The bundled wheel is built with `make build-bundle` and includes compiled UI assets baked into the package.

## Makefile

### Development

```bash
make dev-backend       # start FastAPI in live mode (port 8001), reload on source changes
make dev-frontend      # start Vite dev server (port 5173) with HMR
make dev-bundle        # build UI, serve full bundled experience at port 8001 via uv run
```

Standard development uses `dev-backend` + `dev-frontend` in separate terminals. The Vite dev server proxies nothing — the frontend calls the backend at `http://localhost:8001` directly via CORS.

`dev-bundle` is useful for testing the bundled UI experience without building a wheel. It copies `ui/dist` into the source tree temporarily and cleans up when the server exits.

### Building

```bash
make build             # build core wheel → dist/agentevals-*.whl
make build-bundle      # build UI, embed into wheel, clean up → dist/agentevals-*.whl
make build-ui          # build React app only → ui/dist/
```

Both `build` and `build-bundle` produce `dist/agentevals-*.whl` with the same package name and version. The difference is that `build-bundle` embeds `ui/dist/` as `agentevals/_static/` inside the wheel. The hatchling `artifacts` config ensures the gitignored `_static/` directory is included.

### Testing and cleanup

```bash
make test              # run pytest
make clean             # remove dist/, build/, ui/dist/, src/agentevals/_static/
```

## Runtime behavior

The serve command auto-detects the active mode:

- `agentevals serve` — REST-only if no bundled UI present; full experience if bundled wheel
- `agentevals serve --dev` — always enables live mode (WebSocket + streaming + sessions)
- `agentevals serve --headless` — disables UI serving even in bundled builds (API-only)

Controlled by environment variables `AGENTEVALS_LIVE=1` and `AGENTEVALS_HEADLESS=1`, which the CLI sets automatically based on flags and detected `_static/` presence.

## NixOS / Nix devshell

The project provides a `flake.nix` devshell. Inside the Nix environment, `agentevals` in PATH points to the Nix store derivation (immutable). Use `uv run` to run from the live source tree:

```bash
uv run agentevals serve --dev    # live source, dev mode
make dev-bundle                   # live source, bundled UI test
```

To release a new Nix derivation, update `flake.nix` with the new version and rebuild.

## Releasing

1. Bump `version` in `pyproject.toml`
2. Commit and push the change
3. Tag and push — this triggers the release workflow automatically:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
4. Alternatively, trigger manually from **GitHub → Actions → Release → Run workflow** and enter the tag

The workflow (`.github/workflows/release.yml`) runs `make release`, which produces two named wheels in `dist/`:

```
dist/agentevals-0.1.0-core-py3-none-any.whl    # CLI + REST API
dist/agentevals-0.1.0-bundle-py3-none-any.whl  # CLI + REST API + streaming + embedded UI
```

Both are attached as artifacts to the GitHub Release. Users download the appropriate wheel:

```bash
pip install "agentevals-0.1.0-core-py3-none-any.whl"
pip install "agentevals-0.1.0-bundle-py3-none-any.whl[live]"
```
