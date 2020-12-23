# OpenAPI generated server

Spring Boot Server 


## Overview  
This server was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.
By using the [OpenAPI-Spec](https://openapis.org), you can easily generate a server stub.
This is an example of building a OpenAPI-enabled server in Java using the SpringBoot framework.

The underlying library integrating OpenAPI to SpringBoot is [springfox](https://github.com/springfox/springfox)

Start your server as a simple java application

You can view the api documentation in swagger-ui by pointing to  
http://localhost:8080/

Change default port value in application.properties

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# Build application
mvn clean package -Dmaven.test.skip

# Extract the FAT jar
mkdir target/docker-packaging && (cd target/docker-packaging; jar -xf ../*.jar)
```

```bash
# building the image
docker build -t bookservice .

# starting up a container
docker run -p 8080:8080 bookservice
```

and open your browser to here:

```
http://localhost:8080/
```