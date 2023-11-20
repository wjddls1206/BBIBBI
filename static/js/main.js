function checkLogin() {
  if (!userIsAuthenticated) {
    alert("로그인이 필요한 서비스입니다. 로그인 페이지로 이동합니다.");
    window.location.href = loginUrl;
  }
}
