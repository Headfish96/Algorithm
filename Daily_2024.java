import java.util.Scanner;

public class Daily_2024 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] map = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		
		for(int i = 0; i< n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
			
		int[][] deltas = {{-1,0},{1,0},{0,-1},{0,1}};
		
		int maxsum = 0;
		for(int r = 0; r < n; r++) {
			for(int c = 0; c < n; c++) {
				int sum = map[r][c];
				for(int i = 0; i < deltas.length; i++) {
					int nr = r + deltas[i][0];
					int nc = c + deltas[i][1];
					if(nr>=0 && nr < n && nc >= 0 && nc < n) {
						sum += map[nr][nc];
					}
				if(sum >= maxsum) {
					maxsum = sum;
				}
			}
		}
	}
	System.out.println(maxsum);
}
}
