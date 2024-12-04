import Image from "next/image";
import Link from "next/link";

export default function Nav() {
  return (
    <nav className="fixed w-full bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800 z-50">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2">
          <Image src="/pygyat.png" alt="PyGyat Logo" width={32} height={32} />
          <span className="font-bold text-xl">PyGyat</span>
        </Link>
        <div className="flex gap-6">
          <Link href="/docs" className="hover:text-purple-600">Documentation</Link>
          <a href="https://pypi.org/project/pygyat/" className="hover:text-purple-600">PyPI</a>
          <a href="https://github.com/shamith09/pygyat" className="hover:text-purple-600">GitHub</a>
          <a href="https://marketplace.visualstudio.com/items?itemName=shamith-pasula.vscode-pygyat" className="hover:text-purple-600">VS Code Marketplace</a>
        </div>
      </div>
    </nav>
  );
} 