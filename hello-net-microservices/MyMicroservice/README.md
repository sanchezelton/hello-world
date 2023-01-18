
# Description

This is a microservice built on .NET Core 7.0, based on [.NET Tutorial - Your First Microservice](https://dotnet.microsoft.com/en-us/learn/aspnet/microservice-tutorial/intro). In addition, to the randomized non-DB backed WeatherForecast microservice, this aims to provide a user API for registration,
activation, login, user preferences, user details, account deletion, and password reset.

# User stories

Like hello-microservices, this aims to extend the API to support the following use cases:

1. As a user, I shall be able to register myself by creating a new account in the system.
2. As a user, I will have to activate my account by using the activation link sent to my email address before using the various api services.
3. As a registered and activated user, I shall be able to login into the system using my valid credentials.
4. As an authenticated user, I shall be able to add or modify my shopping preferences in my account.
5. As a user, I shall be able to reset my password.
6. As an authenticated user, I shall be able to see my personal details including my preferences in the system database.
7. As an authenticated user, I shall be able to delete my account in the system permanently.

# Requirements

[.NET 7 SDK (64-bit)](https://download.visualstudio.microsoft.com/download/pr/17798684-12da-417d-845b-8d2f54b3bd67/d6a67ffe06f263906571aacf7057bc8e/dotnet-sdk-7.0.102-osx-x64.pkg)

Arm64 download [also available](https://download.visualstudio.microsoft.com/download/pr/dfbffbab-2187-44a8-b911-308136f001c1/8c754f776f6a476f6ab6681d72d88b2e/dotnet-sdk-7.0.102-osx-arm64.pkg)

# How to use

1. Build the project to resolve dependencies.

`dotnet build`

2. Run the project directly (this will build if not already done)

`dotnet run`

If in case you wish to create the base service yourself (without the above user stories addressed and only with the WeatherForecast microservice), run:

`dotnet new webapi -o <name-of-your-microservice> --no-https -f net7.0`

# Docker container

You may also run the microservice within a Docker container using the included Dockerfile as follows:

1. Create docker image

`docker build -t <your-chosen-image-tag-name> .`

2. Then run the image in a container

`docker run -it --rm -p <port>:80 --name <your-chosen-container-name> <your-chosen-image-tag-name>`

The microservices endpoint will be running at http://localhost:<port>/<api-endpoint>
