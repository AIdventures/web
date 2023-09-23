export function formatDate(dateString:string) {
    const [day, month, year] = dateString.split("/");
    const options = { year: "numeric", month: "long", day: "numeric" } as const;
    const date = new Date(`${year}-${month}-${day}`);
    return date.toLocaleDateString(undefined, options);
}
