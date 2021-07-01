FROM mcr.microsoft.com/dotnet/runtime:5.0-focal AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:5.0-focal AS build
WORKDIR /src
COPY ["logisticsFrontend/logisticsFrontend.csproj", "logisticsFrontend/"]
RUN dotnet restore "logisticsFrontend\logisticsFrontend.csproj"
COPY . .
WORKDIR "/src/logisticsFrontend"
RUN dotnet build "logisticsFrontend.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "logisticsFrontend.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "logisticsFrontend.dll"]
