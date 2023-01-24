using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Connect to PostgreSQL DB
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
if (connectionString == null) {
    throw new Exception("No connection string provided!");
}
builder.Services.AddDbContext<HelloMicroserviceDb>(options =>
    options.UseNpgsql(connectionString)
);

// helps capture database-related exceptions along with possible actions to resolve those in the HTML response format
builder.Services.AddDatabaseDeveloperPageExceptionFilter();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();

app.MapControllers();

app.Run();

record User(int id) {
    public string email {get;set;} = default!;
    public string password {get;set;} = default!;
    public string firstName {get;set;} = default!;
    public string lastName {get;set;} = default!;
    public int dob {get;set;} = default!;
    public bool active {get;set;} = default!;
    public int activationCode {get;set;} = default!;
    public int createdAt {get;set;} = default!;
    public int updatedAt {get;set;} = default!;
}

record ShoppingPreference(int id) {
    public string name {get;set;} = default!;
}

record PasswordRequest(int id) {
    public string resetKey {get;set;} = default!;
    public string email {get;set;} = default!;
    public int createdAt {get;set;} = default!;
}

class HelloMicroserviceDb : DbContext {
    public HelloMicroserviceDb(DbContextOptions<HelloMicroserviceDb> options): base(options) {

    }
    public DbSet<User> Users => Set<User>();
    public DbSet<ShoppingPreference> ShoppingPreferences => Set<ShoppingPreference>();
    public DbSet<PasswordRequest> PasswordRequests => Set<PasswordRequest>();
}
