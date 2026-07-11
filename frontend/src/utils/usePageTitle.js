import { useEffect } from "react";

export default function usePageTitle(title) {

    useEffect(() => {

        const previousTitle = document.title;

        document.title = title

            ? `${title} | Intelligent Security Analytics`

            : "Intelligent Security Analytics Platform";

        return () => {

            document.title = previousTitle;

        };

    }, [title]);

}
