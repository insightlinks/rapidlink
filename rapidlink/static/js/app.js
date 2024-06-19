window.addEventListener("DOMContentLoaded", (event) => {
  const getNode = document.querySelector.bind(document);

  const signinform = getNode("#signin");
  const unsigninContainer = signinform;
  const signinedContainer = getNode(".signedin-container");

  const createLinkform = getNode("#createlinkform");
  const previewLinkBtn = getNode(".preview-btn");
  const signoutBtn = getNode("#signout");

  signoutBtn.addEventListener("click", (event) => {
    event.preventDefault();
    unsigninContainer.removeAttribute("hidden");
    signinedContainer.setAttribute("hidden", "hidden");
    localStorage.removeItem("user_profile");
    signinform.reset();
  });

  signinform.addEventListener("submit", (event) => {
    event.preventDefault();
    const userformdata = new FormData(signinform);
    fetch("/auth/signin", { method: "POST", body: userformdata })
      .then((res) => {
        if (res.status === 401) {
          return Promise.reject(new Error("Unauthorized"));
        }
        return res.json();
      })
      .then((result) => {
        if (result.code !== 200) {
          return Promise.reject(new Error(result.message || "Unknown error"));
        }
        unsigninContainer.setAttribute("hidden", "hidden");
        signinedContainer.removeAttribute("hidden");
        signinedContainer.querySelector(".username").textContent =
          result.data.user.username;
        localStorage.setItem("user_profile", JSON.stringify(result.data));
        alert("Signin successful");
      })
      .catch((err) => {
        alert("Signin failed: " + err.message);
      });
  });

  createLinkform.addEventListener("submit", (event) => {
    event.preventDefault();
    const user_profile = JSON.parse(localStorage.getItem("user_profile")) || {};
    if (!user_profile) {
      alert("Please signin first");
      return;
    }
    const linkformdata = new FormData(createLinkform);
    fetch("/api/links", {
      method: "POST",
      body: linkformdata,
      headers: {
        Authorization: `Bearer ${user_profile.access_token}`,
      },
    })
      .then((res) => {
        if (res.status === 401) {
          alert("Unauthorized");
          return Promise.reject(new Error("Unauthorized"));
        }
        return res.json();
      })
      .then((result) => {
        if (result.code !== 200) {
          return Promise.reject(new Error(result.message || "Unknown error"));
        }
        alert("Link created successfully");
        createLinkform.setAttribute("hidden", "hidden");
        previewLinkBtn.removeAttribute("hidden");
        previewLinkBtn.innerHTML = `<a href="/preview/${result.data.linkid}" target="_blank">
        访问链接: ${window.location.origin}/preview/${result.data.linkid}
        </a>`;
      })
      .catch((err) => {
        alert("Link creation failed: " + err.message);
      });
  });
});
