window.addEventListener("DOMContentLoaded", (event) => {
  const getNode = document.querySelector.bind(document);

  const signin = getNode("#signin");
  const createLinkBtn = getNode("#createlink");
  const previewLinkBtn = getNode("#previewlink");

  signin.addEventListener("click", () => {
    const userformdata = new FormData();
    userformdata.append("username", "admin");
    userformdata.append("password", "admin");
    fetch("/auth/signin", { method: "POST", body: userformdata })
      .then((res) => {
        if (res.status === 401) {
          alert("Invalid username or password");
          return;
        }
        return res.json();
      })
      .then((result) => {
        localStorage.setItem("user_profile", result.data || {});
        alert("Signin successful");
      })
      .catch((err) => {
        console.log(err);
        alert("Signin failed");
      });
  });

  createLinkBtn.addEventListener("click", () => {
    const user_profile = localStorage.getItem("user_profile");
    if (!user_profile) {
      alert("Please signin first");
      return;
    }
    const linkformdata = new FormData();
    linkformdata.append("title", "电话消息");
    linkformdata.append("description", "测试通过连接直接拨打电话");
    linkformdata.append("type", "phone");
    linkformdata.append("value", "17002830465");

    fetch("/api/links", { method: "POST", body: linkformdata })
      .then((res) => {
        if (res.status === 401) {
          alert("Unauthorized");
          return;
        }
        return res.json();
      })
      .then((result) => {
        alert("Link created successfully");
      })
      .catch((err) => {
        console.log(err);
        alert("Link creation failed");
      });
  });
});
