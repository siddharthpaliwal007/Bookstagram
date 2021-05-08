/*! For license information please see 11.893af32c.chunk.js.LICENSE.txt */
(this.webpackJsonpBookstagram=this.webpackJsonpBookstagram||[]).push([[11],{236:function(e,t,c){"use strict";var s=c(62),a=c.n(s),n=localStorage.getItem("userToken"),i=a.a.create({baseURL:"http://40.80.95.65/store",headers:{Authorization:"token "+n}});t.a=i},237:function(e,t,c){"use strict";var s=c(2),a=(c(0),c(25)),n=c(7),i=c(63);t.a=Object(n.i)((function(){var e=localStorage.getItem("userType");return Object(s.jsxs)("div",{class:"sidebar",children:[Object(s.jsx)("div",{class:"brand-logo",children:Object(s.jsx)("a",{href:"index.html",children:Object(s.jsx)("img",{src:i.a,alt:"logo",height:"75px",width:"75px"})})}),Object(s.jsxs)("div",{class:"menu",children:["reader"==e?Object(s.jsxs)("ul",{children:[Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/home","data-toggle":"tooltip","data-placement":"right",title:"Home",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-home"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/my-books","data-toggle":"tooltip","data-placement":"right",title:"My book Shelf",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-library"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/book-list","data-toggle":"tooltip","data-placement":"right",title:"List Of Books",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-book"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/my-friends","data-toggle":"tooltip","data-placement":"right",title:"My Friends",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-user-group"})})})}),Object(s.jsx)("li",{class:"logout",children:Object(s.jsx)("a",{href:"signin.html","data-toggle":"tooltip","data-placement":"right",title:"Signout",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-power"})})})})]}):Object(s.jsxs)("ul",{children:[Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/","data-toggle":"tooltip","data-placement":"right",title:"Home",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-home"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/uploadbook","data-toggle":"tooltip","data-placement":"right",title:"upload a book",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-library"})})})}),Object(s.jsx)("li",{class:"logout",children:Object(s.jsx)("a",{href:"signin.html","data-toggle":"tooltip","data-placement":"right",title:"Signout",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-power"})})})})]}),Object(s.jsxs)("p",{class:"copyright",children:["\xa9 ",Object(s.jsx)("a",{href:"#",children:"Bookstagram INC"})]})]})]})}))},239:function(e,t,c){"use strict";c.p},240:function(e,t,c){"use strict";var s=c(19),a=c(2),n=c(0),i=c.n(n),o=c(34),r=(c(239),c(237)),l=c(15),j=c(25),d=c(236),b=c(45);Object.size=function(e){var t,c=0;for(t in e)e.hasOwnProperty(t)&&c++;return c};t.a=function(){JSON.parse(localStorage.getItem("userData"));var e=Object(n.useState)([]),t=Object(s.a)(e,2),c=t[0],u=t[1],h=Object(n.useState)(!1),O=Object(s.a)(h,2),m=O[0],p=O[1],f=Object(n.useState)(),x=Object(s.a)(f,2),g=(x[0],x[1]),v=Object(n.useState)(),N=Object(s.a)(v,2),y=N[0],S=N[1],k=Object(n.useState)(!1),w=Object(s.a)(k,2),E=w[0],F=w[1],I=Object(o.b)(),C=(Object(o.c)((function(e){return e})),localStorage.getItem("dp")),B=localStorage.getItem("email");Object(n.useEffect)((function(){void 0!=localStorage.getItem("notification")?S(localStorage.getItem("notification")):S(0),T()}),[y]);var T=function(){var e=localStorage.getItem("userId");d.a.get("/userfeed/?pk="+e,{notify_type:"Ticker Notification"}).then((function(e){200===e.status&&(console.log("Response",Object.size(e.data)),u(e.data),b.a.success("User Books Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0})),console.log("Notify",y),localStorage.setItem("notification",Object.size(e.data)-y)})).catch((function(e){g(e),console.error("Error",e),g("This Books Fetch Failed")}))};return Object(a.jsxs)(i.a.Fragment,{children:[Object(a.jsx)("div",{className:"header",children:Object(a.jsx)("div",{className:"container",children:Object(a.jsx)("div",{className:"row",children:Object(a.jsx)("div",{className:"col-xxl-12",children:Object(a.jsxs)("div",{className:"header-content",children:[Object(a.jsxs)("div",{className:"header-right",children:[Object(a.jsx)("div",{className:"brand-logo",children:Object(a.jsxs)("a",{href:"index.html",children:[Object(a.jsx)("img",{src:"./images/logo.png",alt:""}),Object(a.jsx)("span",{children:"Bookstagram"})]})}),Object(a.jsx)("div",{className:"search",children:Object(a.jsx)("form",{action:"#",children:Object(a.jsxs)("div",{className:"input-group",children:[Object(a.jsx)("input",{type:"text",className:"form-control",placeholder:"Search Here"}),Object(a.jsx)("span",{className:"input-group-text",children:Object(a.jsx)("i",{className:"icofont-search"})})]})})})]}),Object(a.jsxs)("div",{className:"header-right",children:[Object(a.jsxs)("div",{className:"dark-light-toggle",onclick:function(){return console.log("Toggle Clicked")},children:[Object(a.jsx)("span",{className:"dark",children:Object(a.jsx)("i",{className:"icofont-moon"})}),Object(a.jsx)("span",{className:"light",children:Object(a.jsx)("i",{className:"icofont-sun-alt"})})]}),Object(a.jsxs)("div",{className:"notification dropdown",children:[Object(a.jsx)("div",{className:"notify-bell",onClick:function(){return F(!E)},children:Object(a.jsx)("span",{children:Object(a.jsx)("i",{className:"icofont-alarm"})})}),E?Object(a.jsxs)("div",{className:"dropdown-menu dropdown-menu-right notification-list",children:[Object(a.jsx)("h4",{children:"Announcements"}),c.length>=1&&c.map((function(e,t){var c=e.publist,s=e.comments,n=e.authorJSON,i=e.buyerJSON,o=e.bookJSON;return Object(a.jsx)("div",{className:"lists",children:Object(a.jsx)("a",{href:"#",className:"",children:Object(a.jsxs)("div",{className:"d-flex align-items-center",children:[Object(a.jsx)("span",{className:"mr-3 icon success",children:Object(a.jsx)("i",{className:"icofont-check"})}),"Book Bought Ticker"===s?Object(a.jsxs)("div",{children:[Object(a.jsx)("p",{children:s}),Object(a.jsx)("br",{}),Object(a.jsxs)("p",{children:[i.first_name," ",i.last_name," Bought book ",o.name," from ",n.first_name," ",n.last_name," "]}),Object(a.jsx)("span",{children:c})]}):Object(a.jsxs)("div",{children:[Object(a.jsx)("p",{children:s}),Object(a.jsx)("br",{}),Object(a.jsx)("p",{children:"Bought book "}),Object(a.jsx)("span",{children:c})]})]})})})}))]}):null]}),Object(a.jsxs)("div",{className:"profile_log dropdown",children:[Object(a.jsxs)("div",{className:"user",onClick:function(){return p(!m)},children:[Object(a.jsx)("span",{className:"thumb",children:Object(a.jsx)("img",{src:C,alt:"profile"})}),Object(a.jsx)("span",{className:"arrow",children:Object(a.jsx)("i",{className:"icofont-angle-down"})})]}),m?Object(a.jsxs)("div",{className:"dropdown-menu dropdown-menu-right",children:[Object(a.jsx)("div",{className:"user-email",children:Object(a.jsxs)("div",{className:"user",children:[Object(a.jsx)("span",{className:"thumb",children:Object(a.jsx)("img",{src:C,alt:"profile"})}),Object(a.jsx)("div",{className:"user-info",children:Object(a.jsx)("span",{children:B})})]})}),Object(a.jsxs)(j.b,{to:"/profile",className:"dropdown-item",children:[Object(a.jsx)("i",{className:"icofont-ui-user"}),"Profile"]}),Object(a.jsxs)(j.b,{to:"/settings-profile",className:"dropdown-item",children:[Object(a.jsx)("i",{className:"icofont-ui-settings"}),"Settings"]}),Object(a.jsxs)("a",{className:"dropdown-item logout",onClick:function(){return localStorage.clear(),I(Object(l.f)()),I(Object(l.b)()),void(window.location.href="/")},children:[Object(a.jsx)("i",{className:"icofont-logout"})," Logout"]})]}):null]})]})]})})})})}),Object(a.jsx)(r.a,{})]})}},243:function(e,t,c){var s;!function(){"use strict";var c={}.hasOwnProperty;function a(){for(var e=[],t=0;t<arguments.length;t++){var s=arguments[t];if(s){var n=typeof s;if("string"===n||"number"===n)e.push(s);else if(Array.isArray(s)&&s.length){var i=a.apply(null,s);i&&e.push(i)}else if("object"===n)for(var o in s)c.call(s,o)&&s[o]&&e.push(o)}}return e.join(" ")}e.exports?(a.default=a,e.exports=a):void 0===(s=function(){return a}.apply(t,[]))||(e.exports=s)}()},244:function(e,t,c){"use strict";c.d(t,"b",(function(){return i})),c.d(t,"c",(function(){return r})),c.d(t,"a",(function(){return l}));var s,a=c(21),n=c.n(a);function i(e,t){return void 0===e&&(e=""),void 0===t&&(t=s),t?e.split(" ").map((function(e){return t[e]||e})).join(" "):e}var o="object"===typeof window&&window.Element||function(){};n.a.oneOfType([n.a.string,n.a.func,function(e,t,c){if(!(e[t]instanceof o))return new Error("Invalid prop `"+t+"` supplied to `"+c+"`. Expected prop to be an instance of Element. Validation failed.")},n.a.shape({current:n.a.any})]);var r=n.a.oneOfType([n.a.func,n.a.string,n.a.shape({$$typeof:n.a.symbol,render:n.a.func}),n.a.arrayOf(n.a.oneOfType([n.a.func,n.a.string,n.a.shape({$$typeof:n.a.symbol,render:n.a.func})]))]);"undefined"===typeof window||!window.document||window.document.createElement;function l(e){var t=typeof e;return null!=e&&("object"===t||"function"===t)}},276:function(e,t,c){"use strict";var s=c(5),a=c(8),n=c(0),i=c.n(n),o=c(21),r=c.n(o),l=c(243),j=c.n(l),d=c(244),b={tag:d.c,fluid:r.a.oneOfType([r.a.bool,r.a.string]),className:r.a.string,cssModule:r.a.object},u=function(e){var t=e.className,c=e.cssModule,n=e.fluid,o=e.tag,r=Object(a.a)(e,["className","cssModule","fluid","tag"]),l="container";!0===n?l="container-fluid":n&&(l="container-"+n);var b=Object(d.b)(j()(t,l),c);return i.a.createElement(o,Object(s.a)({},r,{className:b}))};u.propTypes=b,u.defaultProps={tag:"div"},t.a=u},413:function(e,t,c){"use strict";c.r(t);var s=c(19),a=c(2),n=c(0),i=c.n(n),o=c(236),r=c(45),l=c(276),j=c(7),d=c(237),b=c(240);t.default=Object(j.i)((function(e){var t=Object(n.useState)([]),c=Object(s.a)(t,2),j=c[0],u=c[1],h=Object(n.useState)([]),O=Object(s.a)(h,2),m=O[0],p=O[1],f=Object(n.useState)(),x=Object(s.a)(f,2),g=(x[0],x[1]);Object(n.useEffect)((function(){console.log("From:",e),v()}),[m]);var v=function(){var e=localStorage.getItem("userId");o.a.get("/allfriend/?pk="+e).then((function(e){200===e.status&&(console.log("RESPONSE",e.data),u(e.data),r.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0}))})).catch((function(e){g(e),console.error("Error",e),g("This User Profile Fetch Failed")}))};return Object(a.jsxs)(i.a.Fragment,{children:[Object(a.jsx)(b.a,{}),Object(a.jsx)(d.a,{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)(l.a,{children:Object(a.jsx)("div",{className:"row",children:Object(a.jsx)("div",{className:"col-md-8",children:Object(a.jsxs)("div",{className:"people-nearby",children:[Object(a.jsx)("div",{children:"Search"}),Object(a.jsx)("input",{type:"text",id:"Search",onChange:function(e){return function(e){console.log("Value",e);var t=j.filter((function(t){return console.log("Element",t),t.first_name.toLowerCase().includes(e.toLowerCase())}));console.log("Filtered Data",t),u(t)}(e.target.value)},placeholder:"Search Friends..",title:"Type in a name"}),j.length>=1&&j.map((function(e,t){var c=e.id,s=e.dp,n=e.username,i=(e.first_name,e.usertype),l=e.country;return Object(a.jsx)("div",{className:"nearby-user",children:Object(a.jsxs)("div",{className:"row",children:[Object(a.jsx)("div",{className:"col-md-2 col-sm-2",children:Object(a.jsx)("img",{src:s,alt:"user",className:"profile-photo-lg"})}),Object(a.jsxs)("div",{className:"col-md-7 col-sm-7",children:[Object(a.jsx)("h5",{children:Object(a.jsx)("a",{href:"#",className:"profile-link",children:n})}),Object(a.jsx)("p",{children:i}),Object(a.jsx)("p",{className:"text-muted",children:l})]}),Object(a.jsx)("div",{className:"col-md-3 col-sm-3",children:Object(a.jsx)("button",{className:"btn btn-primary pull-right",onClick:function(e){!function(e){var t=localStorage.getItem("userId");o.a.post("/friend/",{user:t,friend:e,relationship:"addfriend"}).then((function(e){200===e.status&&(console.log("RESPONSE",e.data),p(e.data),r.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0}))})).catch((function(e){g(e),console.error("Error",e),g("This User Profile Fetch Failed")}))}(c)},children:"Add Friend"})})]})})}))]})})})})]})}))}}]);
//# sourceMappingURL=11.893af32c.chunk.js.map