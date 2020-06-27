01 Read, clean, and validate
The first step of almost any data project is to read the data, check for errors and special cases, and prepare data for analysis. This is exactly what you'll do in this chapter, while working with a dataset obtained from the National Survey of Family Growth.

01 Read the codebook
02 Exploring the NSFG data
03 Validate a variable
04 Clean a variable
05 Compute a variable
06 Make a histogram
07 Compute birth weight
08 Filter

02 Distributions
In the first chapter, having cleaned and validated your data, you began exploring it by using histograms to visualize distributions. In this chapter, you'll learn how to represent distributions using Probability Mass Functions (PMFs) and Cumulative Distribution Functions (CDFs). You'll learn when to use each of them, and why, while working with a new dataset obtained from the General Social Survey.

01 Make a PMF
02 Plot a PMF
03 Make a CDF
04 Compute IQR
05 Plot a CDF
06 Distribution of education
07 Extract education levels
08 Plot income CDFs
09 Distribution of income
10 Comparing CDFs
11 Comparing PDFs

03 Relationships
Up until this point, you've only looked at one variable at a time. In this chapter, you'll explore relationships between variables two at a time, using scatter plots and other visualizations to extract insights from a new dataset obtained from the Behavioral Risk Factor Surveillance Survey (BRFSS). You'll also learn how to quantify those relationships using correlation and simple regression.

01 PMF of age
02 Scatter plot
03 Jittering
04 Height and weight
05 Distribution of income
06 Income and height
07 Computing correlations
08 Interpreting correlations
09 Income and vegetables
10 Fit a line

04 Multivariate Thinking
Explore multivariate relationships using multiple regression to describe non-linear relationships and logistic regression to explain and predict binary variables.

01 Regression and causation
02 Using StatsModels
03 Plot income and education
04 Non-linear model of education
05 Making predictions
06 Visualizing predictions
07 Predicting a binary variable


package uas_prktek_java_1;

import java.util.Scanner;

/
 *
 * @author Daratika Pratiwi
 */

public class UAS_Prktek_Java_1_dtp {

    /
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code applSication logic here
        String filem;
        int jml_tiket;
        int harga;
        int bayar;
        Scanner scan = new Scanner(System.in);
    
        System.out.print("Masukkan Filem: ");
        filem = scan.nextLine(); 
        System.out.print("Masukkan jumlah tiket: ");
        jml_tiket = scan.nextInt();
        if(filem == "titanic"){
            harga = 25000;
            if(jml_tiket > 2){
                bayar = (int) (jml_tiket * harga * 0.20);
            } else {
                bayar = jml_tiket * harga;
            }
        } else if(filem == "superman"){
            harga = 15000;
            if(jml_tiket > 2){
                bayar = (int) (jml_tiket * harga * 0.20);
            } else {
                bayar = jml_tiket * harga;
            }
        } else if(filem == "pretty woman"){
            harga = 20000;
            if(jml_tiket > 2){
                bayar = (int) (jml_tiket * harga * 0.20);
            } else {
                bayar = jml_tiket * harga;
            }
        }
        System.out.println("Bayar = Rp. " + bayar);
    }
}