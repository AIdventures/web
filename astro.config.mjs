import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import partytown from '@astrojs/partytown'
import mdx from "@astrojs/mdx";

import sitemap from "@astrojs/sitemap";

import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
  site: 'https://aidventure.es',
  integrations: [
    mdx({
      syntaxHighlight: 'shiki',
      shikiConfig: {
        theme: 'github-dark',
        wrap: true
      },
      drafts: true
    }),
    partytown({
      config: {
        forward: ["dataLayer.push"],
      },
    }),
    tailwind(),
    sitemap()
  ],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex]
  }
});