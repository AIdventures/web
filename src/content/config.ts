import { defineCollection, z } from 'astro:content';
import { image } from 'astro:assets';

const posts = defineCollection({
	schema: ({ image }) => z.object({
		title: z.string(),
		description: z.string(),
		pubDate: z.coerce.date(),
		image: image().optional(),
	}),
});

export const collections = { posts };