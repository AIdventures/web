import { useState, useEffect, useRef } from 'react';
import Fuse, { type FuseResult } from 'fuse.js';

interface Post {
  slug: string;
  data: {
    title: string;
    description: string;
    pubDate: string;
  };
  body: string;
}

export default function Search() {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<FuseResult<Post>[]>([]);
  const [posts, setPosts] = useState<Post[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const modalRef = useRef<HTMLDivElement>(null);

  // Fetch posts on first open
  useEffect(() => {
    if (isOpen && posts.length === 0) {
      setIsLoading(true);
      fetch('/api/search.json')
        .then((res) => res.json())
        .then((data) => {
          setPosts(data);
          setIsLoading(false);
        })
        .catch((err) => {
          console.error('Error fetching search index:', err);
          setIsLoading(false);
        });
    }
  }, [isOpen, posts.length]);

  // Focus input when opened
  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);

  // Handle Search
  useEffect(() => {
    if (posts.length === 0 || query.trim() === '') {
      setResults([]);
      return;
    }

    const fuse = new Fuse(posts, {
      keys: ['data.title', 'data.description', 'body'],
      includeScore: true,
      threshold: 0.4,
      ignoreLocation: true, 
    });

    const searchResults = fuse.search(query);
    setResults(searchResults.slice(0, 5)); // Limit to top 5 results
  }, [query, posts]);

  // Close on Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setIsOpen(false);
      }
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
          e.preventDefault();
          setIsOpen(true);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Close on click outside
  const handleClickOutside = (e: React.MouseEvent) => {
      if (modalRef.current && !modalRef.current.contains(e.target as Node)) {
          setIsOpen(false);
      }
  };

  return (
    <>
      <button
        onClick={() => setIsOpen(true)}
        className="cursor-pointer text-stone-500 hover:text-stone-800 transition-colors p-2 rounded-full hover:bg-stone-100"
        aria-label="Search"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" color="currentColor" fill="none">
            <path d="M15 15L16.5 16.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
            <path d="M16.9333 19.0252C16.3556 18.4475 16.3556 17.5109 16.9333 16.9333C17.5109 16.3556 18.4475 16.3556 19.0252 16.9333L21.0667 18.9748C21.6444 19.5525 21.6444 20.4891 21.0667 21.0667C20.4891 21.6444 19.5525 21.6444 18.9748 21.0667L16.9333 19.0252Z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
            <path d="M16.5 9.5C16.5 5.63401 13.366 2.5 9.5 2.5C5.63401 2.5 2.5 5.63401 2.5 9.5C2.5 13.366 5.63401 16.5 9.5 16.5C13.366 16.5 16.5 13.366 16.5 9.5Z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </button>

      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-start justify-center pt-24 px-4 bg-stone-900/20 backdrop-blur-sm" onClick={handleClickOutside}>
          <div 
            ref={modalRef}
            className="bg-white w-full max-w-lg rounded-xl shadow-2xl overflow-hidden border border-stone-100 flex flex-col max-h-[80vh]"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="p-4 border-b border-stone-100 flex items-center gap-3">
               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5 text-stone-400">
                <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
              </svg>
              <input
                ref={inputRef}
                type="text"
                placeholder="Search posts..."
                className="flex-grow outline-none text-stone-800 placeholder-stone-400 font-sans text-lg bg-transparent"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              />
              <button onClick={() => setIsOpen(false)} className="text-stone-400 hover:text-stone-600 text-sm font-sans px-2 py-1 rounded hover:bg-stone-100">
                ESC
              </button>
            </div>

            <div className="overflow-y-auto p-2">
                {isLoading && <div className="p-4 text-center text-stone-400 font-sans">Loading...</div>}
                
                {!isLoading && query && results.length === 0 && (
                    <div className="p-4 text-center text-stone-400 font-sans">No results found for "{query}"</div>
                )}

                {!isLoading && results.length > 0 && (
                    <ul className="space-y-1">
                        {results.map(({ item }) => (
                            <li key={item.slug}>
                                <a 
                                    href={`/posts/${item.slug}`} 
                                    className="block p-3 hover:bg-stone-50 rounded-lg transition-colors group"
                                    onClick={() => setIsOpen(false)}
                                >
                                    <h3 className="font-serif font-medium text-stone-800 group-hover:text-black">
                                        {item.data.title}
                                    </h3>
                                    <p className="text-sm text-stone-500 font-sans line-clamp-1 mt-1">
                                        {item.data.description}
                                    </p>
                                </a>
                            </li>
                        ))}
                    </ul>
                )}
                 {!isLoading && !query && (
                     <div className="p-4 text-center text-stone-400 text-sm font-sans">
                        Type to search...
                     </div>
                 )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}

