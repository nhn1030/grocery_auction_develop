// sidebar.js

// 각 탭에 클릭 이벤트 리스너 추가
var homeTab = document.getElementById("home-tab");
var dashboardTab = document.getElementById("dashboard-tab");
var ordersTab = document.getElementById("orders-tab");
var productsTab = document.getElementById("products-tab");
var customersTab = document.getElementById("customers-tab");

function setActiveTab(tab) {
    // 모든 탭의 활성화 클래스 제거
    homeTab.classList.remove("active");
    dashboardTab.classList.remove("active");
    ordersTab.classList.remove("active");
    productsTab.classList.remove("active");
    customersTab.classList.remove("active");

    // 선택한 탭에 활성화 클래스 추가
    tab.classList.add("active");
}

homeTab.addEventListener("click", function() {
    setActiveTab(homeTab);
});

dashboardTab.addEventListener("click", function() {
    setActiveTab(dashboardTab);
});

ordersTab.addEventListener("click", function() {
    setActiveTab(ordersTab);
});

productsTab.addEventListener("click", function() {
    setActiveTab(productsTab);
});

customersTab.addEventListener("click", function() {
    setActiveTab(customersTab);
});

// 페이지 로드 시 초기 탭 설정
setActiveTab(homeTab);
