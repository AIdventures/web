# aidventure.es

Astro + MDX blog, built to static files and served by Nginx in a Docker container on a
self-hosted server.

## Publishing — pushing to `main` does NOT deploy

`.github/workflows/deploy.yml` fires only on a `v*` tag (or manual dispatch): it builds the
image, pushes it to GHCR, then SSHes into the server and restarts the `aidventure` container.

```bash
pnpm build                                  # must pass first
git tag --sort=version:refname | tail -1    # current version
git tag v2.0.9 && git push origin v2.0.9
gh run watch $(gh run list --limit 1 --json databaseId -q '.[0].databaseId')
```

Takes ~1m15s; confirm at https://aidventure.es.

If the Dockerfile, `package.json` or the lockfile changed, run `docker build -t aidventure-test .`
locally *before* tagging. CI is otherwise the first place that build ever runs, and it fails
after the tag is already public.

Use pnpm, never npm. The version is pinned in `packageManager` so corepack cannot drift to a
pnpm release that the base image's Node no longer supports — which is exactly how the build
broke once.

## Posts

One `.mdx` in `src/content/posts/`, its images in `src/content/posts/images/<slug>/`.
Frontmatter (schema in `src/content.config.ts`): `title`, `authors`, `tags`, `description`,
`pubDate`, `image`.

- Reuse the existing tag vocabulary instead of inventing tags:
  `grep -h -A12 '^tags:' src/content/posts/*.mdx | grep '^  - ' | sort | uniq -c | sort -rn`
- Emphasis is `<Highlight color="...">`, never a raw `<mark>`.
  Colors: yellow, green, purple, blue, red, orange, brown, cyan.
- Math is KaTeX: `$inline$` and `$$block$$`.
- Close with `## Credits` or `## References`.

## Style

The posts teach a mechanism; they never sell it. In practice:

- Short declarative sentences. No hype, no "in this post we will explore".
- Explain the idea, then show the diagram, then the code — each one earning the next.
- Code goes in small incremental snippets that build one class across several blocks, with
  `# ...` marking what was elided and comments naming tensor shapes. Never one large dump.
  Architecture posts instead collect a single `## Code` section at the end (`resnet.mdx`);
  explanatory posts weave snippets inline (`transformer.mdx`, `attention_layers.mdx`).
- Every section teaches something. Cut whatever exists only for completeness — length is
  never the goal.
- Run the code and check the math before it ships. Nothing gets published unexecuted.
- Wrap prose the way the file being edited already wraps it; posts vary between 60 and 120
  characters, so match the neighbours rather than reflowing.
