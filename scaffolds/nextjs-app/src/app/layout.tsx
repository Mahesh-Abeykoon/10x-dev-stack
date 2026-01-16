import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Next.js App',
  description: 'Modern web application built with Next.js 14',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}