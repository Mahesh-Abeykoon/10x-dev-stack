# 10x Dev Stack Scaffold Copier
# Usage: .\copy-scaffold.ps1 <scaffold-name> <destination>

param(
    [Parameter(Mandatory=$true)]
    [string]$Scaffold,

    [Parameter(Mandatory=$true)]
    [string]$Destination
)

$Source = "scaffolds/$Scaffold"

if (!(Test-Path $Source)) {
    Write-Host "Error: Scaffold '$Scaffold' not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Available scaffolds:"
    Write-Host "  vite-react-optimized"
    Write-Host "  fastapi-agent"
    Write-Host "  minimal-rag-python"
    Write-Host "  mcp-server-starter"
    Write-Host "  nextjs-app"
    Write-Host "  express-api"
    exit 1
}

if (Test-Path $Destination) {
    Write-Host "Error: Destination '$Destination' already exists!" -ForegroundColor Red
    exit 1
}

Write-Host "Copying $Scaffold scaffold to $Destination..."
Copy-Item -Path $Source -Destination $Destination -Recurse

Write-Host "✅ Scaffold copied successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "  cd $Destination"
if (Test-Path "$Destination/package.json") {
    Write-Host "  npm install"
    Write-Host "  npm run dev"
} elseif (Test-Path "$Destination/requirements.txt") {
    Write-Host "  pip install -r requirements.txt"
    Write-Host "  python main.py"
}
Write-Host ""
Write-Host "Happy coding with 10x Dev Stack! 🚀"