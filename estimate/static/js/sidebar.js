// sidebar.js

// 각 탭에 클릭 이벤트 리스너 추가
var productsTab = document.getElementById("selectProductsTab");
var dayAndBulkTab = document.getElementById("conditionForBulkWithDay");
var rangeOfBudgetTab = document.getElementById("rangeOfBudget");
var detailTab = document.getElementById("detail");
var confirmTab = document.getElementById("finalConfirmation");

function setActiveTab(tab) {
    // 모든 탭의 활성화 클래스 제거
    productsTab.classList.remove("active");
    dayAndBulkTab.classList.remove("active");
    rangeOfBudgetTab.classList.remove("active");
    detailTab.classList.remove("active");
    confirmTab.classList.remove("active");

    // 선택한 탭에 활성화 클래스 추가
    tab.classList.add("active");
}

productsTab.addEventListener("click", function() {
    setActiveTab(productsTab);
});

dayAndBulkTab.addEventListener("click", function() {
    setActiveTab(dayAndBulkTab);
});

rangeOfBudgetTab.addEventListener("click", function() {
    setActiveTab(rangeOfBudgetTab);
});

detailTab.addEventListener("click", function() {
    setActiveTab(detailTab);
});

confirmTab.addEventListener("click", function() {
    setActiveTab(confirmTab);
});

// 페이지 로드 시 초기 탭 설정
setActiveTab(productsTab);
