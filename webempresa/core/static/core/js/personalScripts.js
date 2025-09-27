document.addEventListener( 'DOMContentLoaded', () => {

    const navbarElm = document.querySelectorAll('#navbarResponsive a');
    const currentPath = window.location.pathname;
    // const navLinkBlog = navbarElm[5].getAttribute('href');
    // console.log(navLinkBlog)
    // console.log(`[${navLinkBlog}]`, `[${currentPath}]`);
    navbarElm.forEach( navElm => {

        const navLink = navElm.getAttribute('href');

        if( currentPath === navLink ){
            navElm.parentElement.classList.add('active');
        } else {
            navElm.parentElement.classList.remove('active');
        }
        
    });

})
// const nabvarElm = document.querySelectorAll('#navbarResponsive a');