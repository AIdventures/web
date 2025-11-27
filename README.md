# Astro Starter Kit: Minimal

```sh
pnpm create astro@latest -- --template minimal
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
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
| `pnpm install`             | Installs dependencies                            |
| `pnpm dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm build`           | Build your production site to `./dist/`          |
| `pnpm preview`         | Preview your build locally, before deploying     |
| `pnpm astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

## Build and test

Here are the available commands for your Astro blog. To build the project:
```bash
pnpm build
```

This will create a production-ready build in the `dist/` directory. To preview the built site:
```bash
pnpm preview
```

This will serve the production build locally so you can test it before deploying. To run in development mode:
```bash
pnpm dev
```
This runs the dev server with hot reloading (which you're likely already familiar with).


## Highlight colors
```html
<mark style="background: #FFF3A3A6;">  (YELLOW)
<mark style="background: #BBFABBA6;">  (GREEN)
<mark style="background: #ba9375d9;"> -> <mark style="background:rgba(216, 192, 175, 0.85);">  (BROWN)
<mark style="background: #FFB8EBA6;">  (RED)
<mark style="background: #D2B3FFA6;">  (PURPLE)
<mark style="background: #FFB86CA6;">  (ORANGE)
```

## Migration Scripts

To migrate legacy mark tags from posts, use the `scripts/migrate_marks.py` script:

```bash
python3 scripts/migrate_marks.py
```

This script scans `src/content/posts` for MDX files containing `<mark>` tags with specific background colors and replaces them with the `<Highlight>` component.

## To-Review

From time to time need to review:

- Obsidian links `[[` and `]]`.
- Obsidian images `![[`.

## Docker

### Archivos creados
- `Dockerfile`: Utiliza una construcción "multi-stage" (multietapa).
  - Etapas de construcción: Usa Node.js para instalar dependencias y ejecutar pnpm run build.
  - Etapa final: Copia solo la carpeta dist/ resultante a una imagen ligera de Nginx. Esto resulta en una imagen final muy pequeña y rápida, ideal para producción.
- `nginx.conf`: Configuración para que Nginx sirva correctamente tus archivos estáticos, maneje las rutas de carpetas (estándar de Astro) y sirva tu página 404.html personalizada.
- `.dockerignore`: Evita copiar node_modules y otros archivos innecesarios al contexto de Docker.

### Cómo ejecutarlo

1. Construir la imagen de Docker:
Ejecuta el siguiente comando en la terminal (en la raíz de tu proyecto):
```bash
docker build -t my-aesthetic-blog .
```

2. Correr el contenedor una vez construida la imagen, iníciala mapeando el puerto 80 del contenedor al puerto que desees (por ejemplo, 8321):
```bash
docker run -d -p 8321:80 --name my-blog my-aesthetic-blog
```
Verificalo abriendo tu navegador y visita `http://localhost:8321`.

3. Si necesitas detener o eliminar el contenedor más tarde:
```bash
docker stop my-blogdocker
rm my-blog
```

### Configuración de Deployment Automático

Estando ya dentro del servidor, lo más fácil es generar un par de llaves nuevo **específico para GitHub Actions**. Esto es más seguro que usar tus llaves personales.

Sigue estos pasos en tu terminal del servidor:

1.  **Genera las llaves** (dale a Enter a todo para dejarlas sin contraseña, GitHub Actions no soporta llaves con contraseña fácilmente):
    ```bash
    ssh-keygen -t ed25519 -C "github-actions" -f ~/.ssh/github_deploy_key
    ```

2.  **Autoriza la llave pública** para que permita el acceso:
    ```bash
    cat ~/.ssh/github_deploy_key.pub >> ~/.ssh/authorized_keys
    ```

3.  **Obtén la llave PRIVADA** (esta es la que necesitas copiar):
    ```bash
    cat ~/.ssh/github_deploy_key
    ```

Copia **todo** el bloque de texto que salga, incluyendo `-----BEGIN OPENSSH PRIVATE KEY-----` y `-----END OPENSSH PRIVATE KEY-----`. Ese bloque de texto es lo que debes pegar en el secreto `SERVER_SSH_KEY` en GitHub.
