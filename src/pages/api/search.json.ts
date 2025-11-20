import { getCollection } from 'astro:content';

export async function GET() {
  const posts = await getCollection('posts');
  
  const searchList = posts.map((post) => ({
    slug: post.slug,
    data: post.data,
    body: post.body, // Raw MDX content
  }));

  return new Response(JSON.stringify(searchList), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
    },
  });
}

