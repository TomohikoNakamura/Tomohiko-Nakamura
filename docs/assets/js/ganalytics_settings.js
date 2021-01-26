// Global site tag (gtag.js) - Google Analytics
document.write('<script async src="https://www.googletagmanager.com/gtag/js?id={{ config.google_analytics[0] }}"></script>');
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '{{ config.google_analytics[0] }}');

