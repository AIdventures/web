# Astro Starter Kit: Basics

```sh
npm create astro@latest -- --template basics
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/basics)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/basics)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/basics/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

![just-the-basics](https://github.com/withastro/astro/assets/2244813/a0a5533c-a856-4198-8470-2d67b1d7c554)

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── Card.astro
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

- Modify prose elements [here](https://tailwindcss.com/docs/typography-plugin#element-modifiers).
- Live server [cloudflare](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/install-and-setup/tunnel-guide/local)

## 📝 ToDos

- [x] Add a `404` page
- [x] Menu toggler not working on mobile
- [x] Image caption
- [-] Add a `sitemap.xml` [file](https://docs.astro.build/es/guides/integrations-guide/sitemap/)
- [-] Add a `robots.txt` file
- [-] Add RSS
- [x] Add copy-paste code
- [?] Add pagination - Load more
- [x] Add tag filter
- [x] TOC for mobile down the screen collapsible => TOC title touch and expand
- [x] Add Google Analytics (https://www.freecodecamp.org/news/how-to-add-google-analytics-to-your-astro-website/)
- [ ] Add search
- [ ] Responsive test
- [ ] Image optimization
- [ ] Add envio correo suscripción
- [ ] Add a `manifest.json` file

- [ ] Fix "our/we" y otras palabras personales en los posts

```astro
<!-- Add a Load More button here -->
<div class=`
    cursor-pointer
    flex
    items-center
    justify-center
    w-48
    my-6
    px-5
    py-3
    mx-auto
    focus:outline-none
    focus:ring-2
    focus:ring-black
    focus:ring-offset-2
    rounded-xl
    font-medium
    border-black
    border-2
    bg-black
    text-base
    text-white
    hover:bg-lila-500
    hover:text-black
`>
    <button class="btn btn-primary">Load More</button>
</div>
```

https://github.com/danielcgilibert/blog-template


### NGINX Config

```nginx
server {
  server_name   aidventure.es;

  location / {
    proxy_pass  http://localhost:8321;
  }

  location /subscribe {
    proxy_set_header Host $host;
    proxy_pass  http://localhost:8123/subscribe;
  }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/aidventure.es/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/aidventure.es/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = aidventure.es) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


  listen        80;
  server_name   aidventure.es;
    return 404; # managed by Certbot


}
```

## Start the services

```sh
docker compose up --build -d
```

## Design Ideas

- [] Home page redesign:
  - [Two columns, image left](https://dribbble.com/shots/18049946-Web-page-concept-of-bento-shop). 
  - [Two columns, big character right](https://dribbble.com/shots/21954139-Hero-Header-Concept-for-SupaUI-Monster-1).

## Posts Ideas
...