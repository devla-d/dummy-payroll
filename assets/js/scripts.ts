window.addEventListener("load", () => {
  let viewportHeight = window.innerHeight;
  adjustHeight(viewportHeight);
});

window.addEventListener("resize", () => {
  let viewportHeight = window.innerHeight;
  adjustHeight(viewportHeight);
});

const adjustHeight = (height: number) => {
  const dataView = document.querySelectorAll("[data-in-height-viewport]");
  for (let index = 0; index < dataView.length; index++) {
    dataView[index].setAttribute("style", `min-height:${height}px`);
  }
};

document.getElementById("togglesidebar")?.addEventListener("click", (event) => {
  event.preventDefault();
  const sideBar = document.getElementById("sidebar") as HTMLDivElement;

  sideBar.classList.contains("active")
    ? changeToggleIcon(true)
    : changeToggleIcon(false);
  sideBar.classList.toggle("active");
});

const changeToggleIcon = (con: Boolean) => {
  const sideBarToggle = document.getElementById(
    "togglesidebaricon"
  ) as HTMLSpanElement;
  if (con === true) {
    sideBarToggle.classList.remove("fa-times");
    sideBarToggle.classList.add("fa-bars");
  } else {
    sideBarToggle.classList.add("fa-times");
    sideBarToggle.classList.remove("fa-bars");
  }
};
