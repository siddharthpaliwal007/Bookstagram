/*! For license information please see 12.0a50f7db.chunk.js.LICENSE.txt */
(this.webpackJsonpBookstagram=this.webpackJsonpBookstagram||[]).push([[12],{236:function(e,t,c){"use strict";var s=c(62),a=c.n(s),n=localStorage.getItem("userToken"),r=a.a.create({baseURL:"http://40.80.95.65/store",headers:{Authorization:"token "+n}});t.a=r},237:function(e,t,c){"use strict";var s=c(2),a=(c(0),c(25)),n=c(7),r=c(63);t.a=Object(n.i)((function(){var e=localStorage.getItem("userType");return Object(s.jsxs)("div",{class:"sidebar",children:[Object(s.jsx)("div",{class:"brand-logo",children:Object(s.jsx)("a",{href:"index.html",children:Object(s.jsx)("img",{src:r.a,alt:"logo",height:"75px",width:"75px"})})}),Object(s.jsxs)("div",{class:"menu",children:["reader"==e?Object(s.jsxs)("ul",{children:[Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/home","data-toggle":"tooltip","data-placement":"right",title:"Home",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-home"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/my-books","data-toggle":"tooltip","data-placement":"right",title:"My book Shelf",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-library"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/book-list","data-toggle":"tooltip","data-placement":"right",title:"List Of Books",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-book"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/my-friends","data-toggle":"tooltip","data-placement":"right",title:"My Friends",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-user-group"})})})}),Object(s.jsx)("li",{class:"logout",children:Object(s.jsx)("a",{href:"signin.html","data-toggle":"tooltip","data-placement":"right",title:"Signout",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-power"})})})})]}):Object(s.jsxs)("ul",{children:[Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/","data-toggle":"tooltip","data-placement":"right",title:"Home",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-ui-home"})})})}),Object(s.jsx)("li",{children:Object(s.jsx)(a.b,{to:"/uploadbook","data-toggle":"tooltip","data-placement":"right",title:"upload a book",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-library"})})})}),Object(s.jsx)("li",{class:"logout",children:Object(s.jsx)("a",{href:"signin.html","data-toggle":"tooltip","data-placement":"right",title:"Signout",children:Object(s.jsx)("span",{children:Object(s.jsx)("i",{class:"icofont-power"})})})})]}),Object(s.jsxs)("p",{class:"copyright",children:["\xa9 ",Object(s.jsx)("a",{href:"#",children:"Bookstagram INC"})]})]})]})}))},239:function(e,t,c){"use strict";c.p},240:function(e,t,c){"use strict";var s=c(19),a=c(2),n=c(0),r=c.n(n),i=c(34),o=(c(239),c(237)),l=c(15),j=c(25),d=c(236),b=c(45);Object.size=function(e){var t,c=0;for(t in e)e.hasOwnProperty(t)&&c++;return c};t.a=function(){JSON.parse(localStorage.getItem("userData"));var e=Object(n.useState)([]),t=Object(s.a)(e,2),c=t[0],u=t[1],h=Object(n.useState)(!1),O=Object(s.a)(h,2),m=O[0],p=O[1],f=Object(n.useState)(),g=Object(s.a)(f,2),x=(g[0],g[1]),v=Object(n.useState)(),N=Object(s.a)(v,2),S=N[0],y=N[1],k=Object(n.useState)(!1),w=Object(s.a)(k,2),E=w[0],C=w[1],F=Object(i.b)(),P=(Object(i.c)((function(e){return e})),localStorage.getItem("dp")),I=localStorage.getItem("email");Object(n.useEffect)((function(){void 0!=localStorage.getItem("notification")?y(localStorage.getItem("notification")):y(0),B()}),[S]);var B=function(){var e=localStorage.getItem("userId");d.a.get("/userfeed/?pk="+e,{notify_type:"Ticker Notification"}).then((function(e){200===e.status&&(console.log("Response",Object.size(e.data)),u(e.data),b.a.success("User Books Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0})),console.log("Notify",S),localStorage.setItem("notification",Object.size(e.data)-S)})).catch((function(e){x(e),console.error("Error",e),x("This Books Fetch Failed")}))};return Object(a.jsxs)(r.a.Fragment,{children:[Object(a.jsx)("div",{className:"header",children:Object(a.jsx)("div",{className:"container",children:Object(a.jsx)("div",{className:"row",children:Object(a.jsx)("div",{className:"col-xxl-12",children:Object(a.jsxs)("div",{className:"header-content",children:[Object(a.jsxs)("div",{className:"header-right",children:[Object(a.jsx)("div",{className:"brand-logo",children:Object(a.jsxs)("a",{href:"index.html",children:[Object(a.jsx)("img",{src:"./images/logo.png",alt:""}),Object(a.jsx)("span",{children:"Bookstagram"})]})}),Object(a.jsx)("div",{className:"search",children:Object(a.jsx)("form",{action:"#",children:Object(a.jsxs)("div",{className:"input-group",children:[Object(a.jsx)("input",{type:"text",className:"form-control",placeholder:"Search Here"}),Object(a.jsx)("span",{className:"input-group-text",children:Object(a.jsx)("i",{className:"icofont-search"})})]})})})]}),Object(a.jsxs)("div",{className:"header-right",children:[Object(a.jsxs)("div",{className:"dark-light-toggle",onclick:function(){return console.log("Toggle Clicked")},children:[Object(a.jsx)("span",{className:"dark",children:Object(a.jsx)("i",{className:"icofont-moon"})}),Object(a.jsx)("span",{className:"light",children:Object(a.jsx)("i",{className:"icofont-sun-alt"})})]}),Object(a.jsxs)("div",{className:"notification dropdown",children:[Object(a.jsx)("div",{className:"notify-bell",onClick:function(){return C(!E)},children:Object(a.jsx)("span",{children:Object(a.jsx)("i",{className:"icofont-alarm"})})}),E?Object(a.jsxs)("div",{className:"dropdown-menu dropdown-menu-right notification-list",children:[Object(a.jsx)("h4",{children:"Announcements"}),c.length>=1&&c.map((function(e,t){var c=e.publist,s=e.comments,n=e.authorJSON,r=e.buyerJSON,i=e.bookJSON;return Object(a.jsx)("div",{className:"lists",children:Object(a.jsx)("a",{href:"#",className:"",children:Object(a.jsxs)("div",{className:"d-flex align-items-center",children:[Object(a.jsx)("span",{className:"mr-3 icon success",children:Object(a.jsx)("i",{className:"icofont-check"})}),"Book Bought Ticker"===s?Object(a.jsxs)("div",{children:[Object(a.jsx)("p",{children:s}),Object(a.jsx)("br",{}),Object(a.jsxs)("p",{children:[r.first_name," ",r.last_name," Bought book ",i.name," from ",n.first_name," ",n.last_name," "]}),Object(a.jsx)("span",{children:c})]}):Object(a.jsxs)("div",{children:[Object(a.jsx)("p",{children:s}),Object(a.jsx)("br",{}),Object(a.jsx)("p",{children:"Bought book "}),Object(a.jsx)("span",{children:c})]})]})})})}))]}):null]}),Object(a.jsxs)("div",{className:"profile_log dropdown",children:[Object(a.jsxs)("div",{className:"user",onClick:function(){return p(!m)},children:[Object(a.jsx)("span",{className:"thumb",children:Object(a.jsx)("img",{src:P,alt:"profile"})}),Object(a.jsx)("span",{className:"arrow",children:Object(a.jsx)("i",{className:"icofont-angle-down"})})]}),m?Object(a.jsxs)("div",{className:"dropdown-menu dropdown-menu-right",children:[Object(a.jsx)("div",{className:"user-email",children:Object(a.jsxs)("div",{className:"user",children:[Object(a.jsx)("span",{className:"thumb",children:Object(a.jsx)("img",{src:P,alt:"profile"})}),Object(a.jsx)("div",{className:"user-info",children:Object(a.jsx)("span",{children:I})})]})}),Object(a.jsxs)(j.b,{to:"/profile",className:"dropdown-item",children:[Object(a.jsx)("i",{className:"icofont-ui-user"}),"Profile"]}),Object(a.jsxs)(j.b,{to:"/settings-profile",className:"dropdown-item",children:[Object(a.jsx)("i",{className:"icofont-ui-settings"}),"Settings"]}),Object(a.jsxs)("a",{className:"dropdown-item logout",onClick:function(){return localStorage.clear(),F(Object(l.f)()),F(Object(l.b)()),void(window.location.href="/")},children:[Object(a.jsx)("i",{className:"icofont-logout"})," Logout"]})]}):null]})]})]})})})})}),Object(a.jsx)(o.a,{})]})}},243:function(e,t,c){var s;!function(){"use strict";var c={}.hasOwnProperty;function a(){for(var e=[],t=0;t<arguments.length;t++){var s=arguments[t];if(s){var n=typeof s;if("string"===n||"number"===n)e.push(s);else if(Array.isArray(s)&&s.length){var r=a.apply(null,s);r&&e.push(r)}else if("object"===n)for(var i in s)c.call(s,i)&&s[i]&&e.push(i)}}return e.join(" ")}e.exports?(a.default=a,e.exports=a):void 0===(s=function(){return a}.apply(t,[]))||(e.exports=s)}()},244:function(e,t,c){"use strict";c.d(t,"b",(function(){return r})),c.d(t,"c",(function(){return o})),c.d(t,"a",(function(){return l}));var s,a=c(21),n=c.n(a);function r(e,t){return void 0===e&&(e=""),void 0===t&&(t=s),t?e.split(" ").map((function(e){return t[e]||e})).join(" "):e}var i="object"===typeof window&&window.Element||function(){};n.a.oneOfType([n.a.string,n.a.func,function(e,t,c){if(!(e[t]instanceof i))return new Error("Invalid prop `"+t+"` supplied to `"+c+"`. Expected prop to be an instance of Element. Validation failed.")},n.a.shape({current:n.a.any})]);var o=n.a.oneOfType([n.a.func,n.a.string,n.a.shape({$$typeof:n.a.symbol,render:n.a.func}),n.a.arrayOf(n.a.oneOfType([n.a.func,n.a.string,n.a.shape({$$typeof:n.a.symbol,render:n.a.func})]))]);"undefined"===typeof window||!window.document||window.document.createElement;function l(e){var t=typeof e;return null!=e&&("object"===t||"function"===t)}},276:function(e,t,c){"use strict";var s=c(5),a=c(8),n=c(0),r=c.n(n),i=c(21),o=c.n(i),l=c(243),j=c.n(l),d=c(244),b={tag:d.c,fluid:o.a.oneOfType([o.a.bool,o.a.string]),className:o.a.string,cssModule:o.a.object},u=function(e){var t=e.className,c=e.cssModule,n=e.fluid,i=e.tag,o=Object(a.a)(e,["className","cssModule","fluid","tag"]),l="container";!0===n?l="container-fluid":n&&(l="container-"+n);var b=Object(d.b)(j()(t,l),c);return r.a.createElement(i,Object(s.a)({},o,{className:b}))};u.propTypes=b,u.defaultProps={tag:"div"},t.a=u},414:function(e,t,c){"use strict";c.r(t);var s=c(19),a=c(2),n=c(0),r=c.n(n),i=c(236),o=c(45),l=c(276),j=c(7),d=c(237),b=c(240);t.default=Object(j.i)((function(e){var t=Object(n.useState)([]),c=Object(s.a)(t,2),j=c[0],u=c[1],h=Object(n.useState)([]),O=Object(s.a)(h,2),m=O[0],p=O[1],f=Object(n.useState)([]),g=Object(s.a)(f,2),x=g[0],v=g[1],N=Object(n.useState)([]),S=Object(s.a)(N,2),y=(S[0],S[1],Object(n.useState)()),k=Object(s.a)(y,2),w=(k[0],k[1]),E=Object(n.useState)(),C=Object(s.a)(E,2);C[0],C[1];Object(n.useEffect)((function(){F(),P()}),[x]||!1);var F=function(){var e=localStorage.getItem("userId");i.a.get("/friendlist/"+e+"/").then((function(e){200===e.status&&(console.log("RESPONSE",e.data),u(e.data),o.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0}))})).catch((function(e){w(e),console.error("Error",e),w("This User Profile Fetch Failed")}))},P=function(){var e=localStorage.getItem("userId");i.a.get("/acceptfriend/"+e+"/").then((function(e){200===e.status&&(console.log("RESPONSE",e.data),p(e.data),o.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0}))})).catch((function(e){w(e),console.error("Error",e),w("This User Profile Fetch Failed")}))};return Object(a.jsxs)(r.a.Fragment,{children:[Object(a.jsx)(b.a,{}),Object(a.jsx)(d.a,{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)("br",{}),Object(a.jsx)(l.a,{children:Object(a.jsx)("div",{className:"row",children:Object(a.jsx)("div",{className:"col-md-8",children:Object(a.jsxs)("div",{className:"people-nearby",children:[Object(a.jsx)("div",{children:"Search"}),Object(a.jsx)("input",{type:"text",id:"Search",onChange:function(e){return function(e){console.log("Value",e);var t=j.filter((function(t){return console.log("Element",t),t.first_name.toLowerCase().includes(e.toLowerCase())}));console.log("Filtered Data",t),u(t)}(e.target.value)},placeholder:"Search Friends..",title:"Type in a name"}),j.length>=1&&j.map((function(e,t){var c=e.id,s=e.dp,n=(e.first_name,e.username),r=(e.last_name,e.usertype),l=e.country;return Object(a.jsx)("div",{className:"nearby-user",children:Object(a.jsxs)("div",{className:"row",children:[Object(a.jsx)("div",{className:"col-md-2 col-sm-2",children:Object(a.jsx)("img",{src:s,alt:"user",className:"profile-photo-lg"})}),Object(a.jsxs)("div",{className:"col-md-7 col-sm-7",children:[Object(a.jsx)("h5",{children:Object(a.jsx)("a",{href:"#",className:"profile-link",children:n})}),Object(a.jsx)("p",{children:r}),Object(a.jsx)("p",{className:"text-muted",children:l})]}),Object(a.jsx)("div",{className:"col-md-3 col-sm-3",children:Object(a.jsx)("button",{className:"btn btn-primary pull-right",onClick:function(e){!function(e){var t=localStorage.getItem("userId");i.a.get("/unfriend/?pk="+t+"&friend="+e).then((function(e){200===e.status&&(console.log("RESPONSE",e.data),o.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0})),window.location.reload(!1)})).catch((function(e){w(e),console.error("Error",e),w("This User Profile Fetch Failed")}))}(c)},children:"Remove Friend"})})]})})})),m.length>=1&&m.map((function(e,t){var c=e.id,s=e.username,n=(e.first_name,e.last_name,e.usertype),r=e.country;return Object(a.jsx)("div",{className:"nearby-user",children:Object(a.jsxs)("div",{className:"row",children:[Object(a.jsx)("div",{className:"col-md-2 col-sm-2",children:Object(a.jsx)("img",{src:"https://bootdey.com/img/Content/avatar/avatar7.png",alt:"user",className:"profile-photo-lg"})}),Object(a.jsxs)("div",{className:"col-md-7 col-sm-7",children:[Object(a.jsx)("h5",{children:Object(a.jsx)("a",{href:"#",className:"profile-link",children:s})}),Object(a.jsx)("p",{children:n}),Object(a.jsx)("p",{className:"text-muted",children:r})]}),Object(a.jsx)("div",{className:"col-md-3 col-sm-3",children:Object(a.jsx)("button",{className:"btn btn-primary pull-right",onClick:function(e){!function(e){var t=localStorage.getItem("userId");i.a.put("/friendupdate/",{user:t,friend:e,relationship:"friends"}).then((function(e){200===e.status&&(console.log("RESPONSE",e.data),v(e.data),o.a.success("User Profile Fetch Successful",{position:"top-right",autoClose:3e3,hideProgressBar:!0,closeOnClick:!0,pauseOnHover:!0,draggable:!0,progress:void 0}),window.location.reload(!1))})).catch((function(e){w(e),console.error("Error",e),w("This User Profile Fetch Failed")}))}(c)},children:"Accept Request"})})]})})}))]})})})})]})}))}}]);
//# sourceMappingURL=12.0a50f7db.chunk.js.map