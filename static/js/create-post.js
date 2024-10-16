
function PostAlert() {
  const postButton = document.getElementById("create-post");

  postButton.addEventListener("click", () => {
     document.getElementById("post-success")="your post has been successfully added to home page"
  });
}