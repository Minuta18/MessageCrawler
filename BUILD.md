1. Copy repository:

```bash
$ git clone https://github.com/Minuta18/MessageCrawler.git
```

2. Set up configuration:

- Change password in `rabbitmq/rabbitmq.env`
- Change port of nginx in `docker-compose.yaml`

3. Install dependencies:

- [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

4. Run using docker compose:

```bash
$ docker compose up --build -d
```


