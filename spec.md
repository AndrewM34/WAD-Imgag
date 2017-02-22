\begin{center} \Large{\underline{WAD2 - Design Specification - Imgag}} \end{center}

\large{\underline{Team C:}}  

Petr Sramek, Archit Gupta, Daniel Šmolík, Andrew Mcnab  

---

\  

\begin{center} \large{\underline{Overview:}} \end{center}
\  

Imgag is quite possibly the greatest image sharing website ever conceived. It's users may share images and videos, and rate them according to their greatness. By using an ingenious algorithm (score = upvotes - downvotes) we can assure our users they will only see the BEST images and videos from across the world.  

In the unlikely event our algorithm does not show the best images possible, we also offer categories, so Imgag's users may see exactly what they desire.  

Users are incentivised to upload incredible images indefinitely, as they will see their score increase as people rate their uploaded images.

\newpage
\begin{center} \large{\underline{User personas:}} \end{center}  
\  

![Pyotr's persona](Pyotr.png)\

\  

![Dimitri's persona](Dimitri.png)\

\newpage
\begin{center} \large{\underline{Specification:}} \end{center}  
\  
\begin{itemize}

\item{Upload and delete images and videos}
\item{Create and delete accounts}
\item{Personalise account}
\item{Like and dislike image and video posts}
\item{View images}
\item{View categories of images and videos}

\end{itemize}

\newpage

\begin{center} \large{\underline{System Architecture Diagram:}} \end{center}
\  

![System architecture diagram](SAD.png)\

\newpage

\begin{center} \large{\underline{ER Diagram:}} \end{center}
\  

![ER diagram](ER.png)\

\newpage

\begin{center} \large{\underline{Wireframes:}}\end{center}
\  

![Categories](viewOfCategories.png)\
![A view of many posts](viewOfManyPosts.png)\
![An image post](viewOfPost.png)\

\newpage

\begin{center} \large{\underline{Walkthrough:}} \end{center}
\  

\underline{URLs:}  

/  
/register/  
/login/  
/login/reset-password/  
/account/  
/account/change-password/  
/categories/  
/categories/\<category_name>\/  
/post/\<post_name>\/  
