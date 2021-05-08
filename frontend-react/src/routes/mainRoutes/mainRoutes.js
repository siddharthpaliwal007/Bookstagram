import React from 'react';

export const userRoutes = [
  {
    path: '/home',
    exact: true,
    name: 'Home',
    component: React.lazy(() => import('../../views/Home/Home')),
  },

  {
    path: '/profile',
    exact: true,
    name: 'Profile',
    component: React.lazy(() => import('../../views/Profile/Profile')),
  },
  {
    path: '/settings-profile',
    exact: true,
    name: 'Settings',
    component: React.lazy(() => import('../../views/Settings/Settings')),
  },
  {
    path: '/my-books',
    exact: true,
    name: 'MyBooks',
    component: React.lazy(() => import('../../views/BookShelf/BookShelf')),
  },
  {
    path: '/book-description',
    exact: true,
    name: 'BooksDescription',
    component: React.lazy(() => import('../../views/BookDescription/BookDescription')),
  },
  {
    path: '/book-list',
    exact: true,
    name: 'BookList',
    component: React.lazy(() => import('../../views/BookList/BookList')),
  },
  {
    path: '/verify-email',
    exact: true,
    name: 'VerifyEmail',
    component: React.lazy(() => import('../../views/VerifyEmail/VerifyEmail')),
  },
  {
    path: '/add-friends',
    exact: true,
    name: 'AddFriends',
    component: React.lazy(() => import('../../views/AddFriends/AddFriends')),
  },
  {
    path: '/my-friends',
    exact: true,
    name: 'MyFriends',
    component: React.lazy(() => import('../../views/MyFriends/MyFriends')),
  },
  {
    path: '/news-feed',
    exact: true,
    name: 'NewsFeed',
    component: React.lazy(() => import('../../views/NewsFeed/NewsFeed')),
  },
  {
    path: '/referral-tree',
    exact: true,
    name: 'ReferralTree',
    component: React.lazy(() => import('../../views/ReferralTree/ReferralTree')),
  },
  {
    path: '/account-locked',
    exact: true,
    name: 'AccountLocked',
    component: React.lazy(() => import('../../views/AccountLocked/AccountLocked')),
  },
  {
    path: '/uploadbook',
    exact: true,
    name: 'UploadBook',
    component: React.lazy(() => import('../../views/UploadBook/UploadBook')),
  }, 
   // Main route's default dashboard
  {
    redirectRoute: true,
    name: 'homeRedirect',
    path: '/home',
  },
];
