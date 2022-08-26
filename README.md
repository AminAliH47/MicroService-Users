<div align="center">

# MicroService Project
### _Users service_

<hr>
</div>

In this service, you can manage Database queries and django gRPC framework core.

**Gateway service** connect to **Users service** with **gRPC**,
It receives the data from the Users service.

## ⚠ Important ⚠
Before you run Gateway service, you should run this service to connect correctly with gRPC.

[Gateway Service](https://github.com/AminAliH47/MicroService-Gateway)

<hr>

## 🏁 Run the service
**Users service is dockerized.** 
This means that the running of the project is very simple.

⚠ Naturally, Docker must be installed on your system. [Install docker](https://docs.docker.com/get-docker/)

<br>

⚠ For the initial execution of the services,
you need to enter the following command in the terminal to create the Docker network.
```commandline
$ docker network create users_network -d bridge --gateway 10.5.0.1 --subnet 10.5.0.0/16
```

⚠ Before you build project in Docker, you need to create `dbdata` directory to save database
datas in this folder.

So run this command in the main root of project:

linux/macOS:
```commandline
$ mkdir ./dbdata
```

After that run this command in the main root of project:

linux/macOS:
```commandline
$ docker-compose up --build -d
```

After you run service correctly, You should run [Gateway Service](https://github.com/AminAliH47/MicroService-Gateway) 
to perform CRUD operation with Restfull API.

<hr>

## ✅ Use the project
Now you should run [Gateway Service](https://github.com/AminAliH47/MicroService-Gateway) to use services.
> You can read documentation of Gateway service on its GitHub page

<div align="center">
<br>

###### Licensed By Huma

</div>