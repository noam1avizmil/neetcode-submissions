  SELECT student_id, MIN(exam_id) AS exam_id, score
  FROM exam_results
  WHERE (student_id, score) IN (
      SELECT student_id, MAX(score)
      FROM exam_results
      GROUP BY student_id
  )
  GROUP BY student_id, score;