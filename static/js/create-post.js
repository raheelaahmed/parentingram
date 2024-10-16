function PostAlert() {
  const postButton = document.getElementById("post-success");

  postButton.addEventListener("click", () => {
    alert("Congratulations! Java is working!");
  });
}