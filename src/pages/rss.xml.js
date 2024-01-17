import { formatDate } from '@/utils';
import rss from '@astrojs/rss';
import { getCollection } from "astro:content";

export async function GET(context) {
    const blog = await getCollection("posts", ({data}) => {
        return data.draft !== true;
    });

    //Transform all dates to date objects
    blog.map((post) => post.data.date = formatDate(post.data.date));

    return rss({
        title: 'AIdventure Blog',
        description: 'Embark on a Journey Through Machine Learning Marvels with AIdventurer',
        site: context.site,
        items: blog.map((post) => ({
            title: post.data.title,
            pubDate: post.data.date,
            description: post.data.description,
            // Calcula el link RSS desde el `slug` del post
            // Este ejemplo asume que todos los posts son renderizados como rutas `/blog/[slug]`
            link: `/blog/${post.slug}/`,
        })),
    });
}
