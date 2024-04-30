CREATE TABLE `useranswer` (
  `question_id` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '''题目序号''',
  `user_answer` varchar(45) COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户 答案',
  `answer_bool` int NOT NULL COMMENT '答题是否正确：0：正确，1：错误',
  `exam_id` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '每次做题的考试ID（每轮）',
  PRIMARY KEY (`question_id`),
  KEY `question_id_idx` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='答题记录'