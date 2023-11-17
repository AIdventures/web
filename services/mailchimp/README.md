docker build -t chimp-subscriber-image .

docker run \
    -it --rm \
    -p 8000:8000 \
    --name chimp-subscriber-container \
    chimp-subscriber-image