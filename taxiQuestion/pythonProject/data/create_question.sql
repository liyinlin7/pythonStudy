CREATE TABLE `questions` (
  `question_id` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '题目序号',
  `number` int NOT NULL COMMENT '序号',
  `question_title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '题目标题',
  `question_answer` varchar(16) COLLATE utf8mb4_general_ci NOT NULL COMMENT '题目答案。A,B,C,B,正确,错误',
  `correct_answer` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '正确答案',
  `type` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '题目分类',
  `question_type` int NOT NULL COMMENT '题目类型。1：选择题，2：判断题，3：服务五句话 ',
  `range` int NOT NULL COMMENT '范围：1：区域，2：全国',
  `collect` int GENERATED ALWAYS AS (1) VIRTUAL COMMENT '是否收藏。0：收藏，1：没收藏',
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci