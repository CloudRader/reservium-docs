# Update Reservium on Docker

It is recommended that users pull the tags pointing to specific reservium versions when running in environments other than testing.

To update reservium, change the image tag in your docker-compose.yml file:

For api:

```yaml
 image: darkrader/reservium-api:<IMAGE_TAG>
```

For ui:

```yaml
 image: darkrader/reservium-ui:<IMAGE_TAG>
```

Then pull the latest image and relaunch your containers:

```bash
docker compose pull
docker compose up -d
```

!!! warning 

    The 'latest' tag does not automatically keep your container up to date. You must run docker compose pull to fetch the latest image version before updating.

By doing this:

- a new reservium docker image will be pulled and a new container created