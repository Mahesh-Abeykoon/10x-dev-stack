import { Terminal } from 'lucide-react';

function App() {
    return (
        <div className="min-h-screen bg-neutral-950 text-white flex items-center justify-center p-4">
            <div className="max-w-md w-full bg-neutral-900 border border-neutral-800 rounded-xl p-8 shadow-2xl">
                <div className="flex items-center gap-3 mb-6">
                    <div className="p-3 bg-blue-500/10 rounded-lg">
                        <Terminal className="w-6 h-6 text-blue-400" />
                    </div>
                    <h1 className="text-xl font-bold tracking-tight">10x Dev Stack</h1>
                </div>

                <p className="text-neutral-400 mb-6 leading-relaxed">
                    This is a minimalist, AI-friendly React scaffold.
                    It comes pre-configured with Tailwind, strict TypeScript, and no unnecessary bloat.
                </p>

                <div className="space-y-3">
                    <div className="h-2 w-1/3 bg-neutral-800 rounded-full animate-pulse" />
                    <div className="h-2 w-2/3 bg-neutral-800 rounded-full animate-pulse delay-75" />
                    <div className="h-2 w-1/2 bg-neutral-800 rounded-full animate-pulse delay-150" />
                </div>

                <div className="mt-8 pt-6 border-t border-neutral-800 flex justify-between text-xs text-neutral-500 font-mono">
                    <span>src/App.tsx</span>
                    <span>Ready to build</span>
                </div>
            </div>
        </div>
    )
}

export default App
