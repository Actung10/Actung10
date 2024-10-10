// pages/search/search.js
Page({
  data: {
    filteredProjects: [], // 搜索过滤后的项目列表
    noResult: false, // 是否显示未搜索到结果的提示
  },

  onLoad: function(options) {
    // 获取传递过来的搜索关键词
    const query = decodeURIComponent(options.query || '');
    const app = getApp();
    const allProjects = app.globalData.projects;

    if (query) {
      // 过滤项目列表，匹配项目名称、发起人、指导教师
      const filteredProjects = allProjects.filter(project =>
        project.name.toLowerCase().includes(query) ||
        project.initiator.toLowerCase().includes(query) ||
        project.mentor.toLowerCase().includes(query)
      );

      this.setData({
        filteredProjects,
        noResult: filteredProjects.length === 0, // 如果过滤后的项目列表为空，则显示未搜索到结果的提示
      });
    } else {
      // 如果没有传递搜索关键词，则不显示任何项目
      this.setData({
        filteredProjects: [],
        noResult: true,
      });
    }
  },

  goBack() {
    wx.navigateBack({
      delta: 1
    });
  },
});