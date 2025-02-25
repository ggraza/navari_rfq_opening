frappe.listview_settings["Committee Note"] = {
  formatters: {
    note_type(val) {
      if (val === "Opening Minutes") {
        return "<span class='indicator-pill yellow'>" + __(val) + "</span>";
      } else if (val === "Evaluation Minutes") {
        return "<span class='indicator-pill purple'>" + __(val) + "</span>";
      } else {
        return "<span class='indicator-pill green'>" + __(val) + "</span>";
      }
    },
  },
};
