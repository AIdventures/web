// 1. Import utilities from `astro:content`
import {z, defineCollection} from "astro:content";

// 2. Define your content schema
// https://docs.astro.build/en/guides/content-collections/#defining-datatypes-with-zod
const postsCollection = defineCollection({
    schema: ({image}) => z.object({
        author: z.string(),
        date: z.string(),
        image: image(),
        title: z.string(),
        description: z.string(),
        tags: z.array(z.string()),
        draft: z.boolean().optional(),
    }),
})

export const collections = {
    posts: postsCollection,
}