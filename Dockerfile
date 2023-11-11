# https://docs.astro.build/en/recipes/docker/
# docker build -t aidventure-image .
# docker run -d -p 8321:4321 --name aidventure aidventure-image
FROM node:18-buster AS runtime
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm
RUN npm install -g http-server

COPY . .

RUN pnpm install
RUN pnpm run build

ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD http-server -p 4321 dist
