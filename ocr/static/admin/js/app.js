let plusEle = document.querySelector(
  "#reminders .container .section-title svg"
);

let boxEle = document.querySelector(
  "#reminders .container .section-title .box"
);

let formEle = document.querySelector(
  "#reminders .container .section-title form"
);

let saveEle = document.querySelector(
  "#reminders .container .section-title form input[type='submit']"
);
plusEle.addEventListener(
  "click",
  function () {
    boxEle.classList.add("active-box");
  },
  true
);

// close Ele
let CloseEle = document.querySelectorAll(".close");

CloseEle[0].addEventListener(
  "click",
  function () {
    boxEle.classList.remove("active-box");
    boxEleTwo.classList.add("none-box");
  },
  true
);

// End close Ele

formEle.addEventListener(
  "submit",
  function (e) {
    let colEle = document.createElement("div");
    colEle.classList.add("col-lg-6");

    let memberEle = document.createElement("div");
    memberEle.classList.add("member", "d-flex", "align-items-start");

    let memberInfoEle = document.createElement("div");
    memberInfoEle.classList.add("member-info");

    let headFourEle = document.createElement("h4");
    let spanEle = document.createElement("span");
    let pragEle = document.createElement("p");
    "a".slice;
    let timeInt = Number.parseInt(timeEle.value);
    let timeVal;
    if (timeInt > 12) {
      timeVal = `${timeInt - 12}${timeEle.value.slice(2)} PM`;
    } else {
      timeVal = `${timeEle.value} AM`;
    }

    let Links = {
      "Alseef Hospital":
        "https://www.bing.com/maps?q=%d9%85%d8%b3%d8%aa%d8%b4%d9%81%d9%89+%d8%a7%d9%84%d8%b3%d9%8a%d9%81&FORM=AWRE",
      "Dar alshifa":
        "https://www.bing.com/maps?&ty=18&q=%D8%AF%D8%A7%D8%A4%20%D8%A7%D9%84%D8%B4%D9%81%D8%A7%D8%A1&ss=ypid.YN8097x2214210955391714468&ppois=29.338396072387695_48.02426528930664_%D8%AF%D8%A7%D8%A4%20%D8%A7%D9%84%D8%B4%D9%81%D8%A7%D8%A1_YN8097x2214210955391714468~&cp=29.338396~48.024265&lvl=16&v=2&sV=1&FORM=SNAPST",
      "Alsalam Hospital":
        "https://www.bing.com/maps?&ty=18&q=hospital%20%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85&ss=ypid.YN8097x16245626079162678796&ppois=29.3688907623291_48.009700775146484_hospital%20%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D9%85_YN8097x16245626079162678796~&cp=29.368891~48.009701&lvl=16&v=2&sV=1&FORM=SNAPST",
      "Hadi Clinic": "https://www.bing.com/maps?q=hospital+hadi&FORM=AWRE",
      "Kuwait Hospital":
        "https://www.bing.com/maps?q=%D9%85%D8%B3%D8%AA%D8%B4%D9%81%D9%89+%D8%A7%D9%84%D9%83%D9%88%D9%8A%D8%AA&go=%D8%A8%D8%AD%D8%AB&qs=ds&form=QBRE",
    };
    headFourEle.innerHTML = "Up-Coming Appointment";
    spanEle.innerHTML = `Date: ${dateEle.value} , ${timeVal} `;
    pragEle.innerHTML = `Dr. ${doctorEle.value}, <a href= ${Links[placeELe.value]}>${placeELe.value}</a>`;
    memberInfoEle.appendChild(headFourEle);
    memberInfoEle.appendChild(spanEle);
    memberInfoEle.appendChild(pragEle);
    memberEle.appendChild(memberInfoEle);
    colEle.appendChild(memberEle);
    rowEle.appendChild(colEle);
    boxEle.classList.remove("active-box");
    e.preventDefault();
  },
  true
);

// Start get value
let dateEle = document.querySelector(".box form .form-one input[type='date']");
let timeEle = document.querySelector(".box form .form-one input[type='time']");
let placeELe = document.querySelector(".box form .form-two select");
let purposeEle = document.querySelector(".box form .form-three select");
let doctorEle = document.querySelector(".box form .form-four input[type='text']");
let noteValueEle = document.querySelector(".box form .form-five textarea").value;
let rowEle = document.querySelector(".row");

// start box two
let plusEleTwo = document.querySelector(".tests .container .section-title svg");
let boxEleTwo = document.querySelector(".tests .container .box-two");

plusEleTwo.addEventListener(
  "click",
  function () {
    boxEleTwo.classList.remove("none-box");
    boxEleTwo.classList.add("active-box");
  },
  true
);

// close box two
CloseEle[1].addEventListener(
  "click",
  function () {
    boxEleTwo.classList.remove("active-box");
    boxEleTwo.classList.add("none-box");
  },
  true
);
// get form page
let formPageOne = document.querySelector(".parent-box .box-two form .form-page-one");
let formPageTwo = document.querySelector(".parent-box .box-two form .form-page-two");

// Continue button
let btnContinue = document.querySelector(".parent-box .box-two form .form-page-one input[value='Continue']");

btnContinue.addEventListener("click", function () {
  formPageOne.classList.add("none-box");
  formPageTwo.classList.remove("none-box");

  // select value
  let selectCategoryEle = document.querySelector(
    ".parent-box .box-two form .form-page-one select#category"
  );

  // label category-text value

  let labelCategoryText = document.querySelector(
    ".parent-box .box-two form .form-page-two label[for='category-text']"
  );
  // (FBS)
  labelCategoryText.innerHTML = selectCategoryEle.value.slice(-5);
  // input category-text value

  let inputCategoryText = document.querySelector(
    ".parent-box .box-two form .form-page-two input#category-text"
  );
  if (selectCategoryEle.value === "Fasting Blood Sugar (FBS)") {
    inputCategoryText.value = 4.3;
  } else if (selectCategoryEle.value === "random Blood Sugar (RBS)") {
    inputCategoryText.value = 5.8;
  } else {
    inputCategoryText.value = "";
  }
  
});

// Goback button
let btnGoback = document.querySelector(".parent-box .box-two form .form-page-two input[value='Goback']");
btnGoback.addEventListener("click", function () {
  formPageOne.classList.remove("none-box");
  formPageTwo.classList.add("none-box");
});
