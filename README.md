

```shell
docker image build -t ubuntu:dbot .
```

Create app
https://discord.com/developers/applications

Click bot, then reveal token. Also use the bot permissiosn calculator

Construct a OAUTH URL:
https://discord.com/oauth2/authorize?client_id=CLIENT_ID_GOES_HERE&scope=bot&permissions=8


## Example manual build
``` shell
docker image build -t bradmorg/ubuntu:dbot /home/pi/discord-bot
docker push bradmorg/ubuntu:dbot 
docker stop discordbot 
docker rm discordbot
docker run --name discordbot --restart always -d -e TOKEN=$TOKEN bradmorg/ubuntu:dbot
```
