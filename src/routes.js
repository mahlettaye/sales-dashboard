import DashboardIcon from "./assets/DashboardIcon.svg";
import DashboardIconActive from "./assets/DashboardIconActive.svg";

import SignOutIcon from "./assets/SignOutIcon.svg";
import AccountsIcon from "./assets/AccountsIcon.svg";
import AccountsIconActive from "./assets/AccountsIconActive.svg";
import Dashboard from "./pages/Dashboard";
//import Accounts from "./pages/Accounts";

import Prediction from "./pages/Prediction";

const routes = [
  {
    label: "Trends",
    path: "/",
    icon: DashboardIcon,
    activeIcon: DashboardIconActive,
    component: Dashboard
  },
  {
    label: "Prediction",
    path: "/Prediction",
    icon: AccountsIcon,
    activeIcon: AccountsIconActive,
    component: Prediction
  },

  {
    label: "Sign Out",
    path: "/sign-out",
    icon: SignOutIcon,
    activeIcon: SignOutIcon
  }
];

export default routes;
