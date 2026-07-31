/**
 * Cloudflare Pages middleware: force apex host (chokmah.me).
 * www is also a custom domain on this Pages project, so a standalone
 * Worker route does not run for that hostname — this middleware does.
 * Fixes Google Search Console "Alternate page with proper canonical tag".
 */
export async function onRequest(context) {
  const url = new URL(context.request.url);

  if (url.hostname === "www.chokmah.me") {
    url.hostname = "chokmah.me";
    url.protocol = "https:";
    return Response.redirect(url.toString(), 301);
  }

  return context.next();
}
